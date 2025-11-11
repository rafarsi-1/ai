from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from .. import schemas, crud, database, llm, models

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/{character_id}", response_model=list[schemas.Message])
def get_chat_history(character_id: int, db: Session = Depends(database.get_db)):
    # Assume user_id=1
    return crud.get_messages(db=db, character_id=character_id, user_id=1)

@router.websocket("/{character_id}")
async def websocket_endpoint(websocket: WebSocket, character_id: int, db: Session = Depends(database.get_db)):
    await websocket.accept()
    character = db.query(models.Character).filter(models.Character.id == character_id).first()
    if not character:
        await websocket.close()
        return

    history = crud.get_messages(db=db, character_id=character_id, user_id=1)  # Load history
    history_msgs = [{"role": "user" if msg.is_user else "assistant", "content": msg.content} for msg in history]

    try:
        while True:
            data = await websocket.receive_text()
            # Save user message
            user_msg = schemas.MessageCreate(content=data, is_user=1)
            crud.create_message(db=db, message=user_msg, character_id=character_id, user_id=1)

            # Generate AI response
            ai_response = llm.generate_response(character.description, history_msgs, data)
            # Save AI message
            ai_msg = schemas.MessageCreate(content=ai_response, is_user=0)
            crud.create_message(db=db, message=ai_msg, character_id=character_id, user_id=1)

            await websocket.send_text(ai_response)
            history_msgs.append({"role": "user", "content": data})
            history_msgs.append({"role": "assistant", "content": ai_response})
    except WebSocketDisconnect:
        pass