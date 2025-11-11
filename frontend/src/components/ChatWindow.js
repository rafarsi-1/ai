import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import axios from 'axios';
import ChatBubble from './ChatBubble';

const socket = io('http://localhost:8000');  // For WebSocket; install socket.io on backend if needed (pip install python-socketio)

const ChatWindow = ({ characterId }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (characterId) {
      axios.get(`http://localhost:8000/chat/${characterId}`).then(res => setMessages(res.data));
      socket.emit('join', characterId);  // Join room; implement on backend if using socket.io

      socket.on('message', (msg) => {
        setMessages(prev => [...prev, { content: msg, isUser: 0 }]);
      });

      return () => socket.off('message');
    }
  }, [characterId]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = () => {
    if (input) {
      socket.emit('chat', { characterId, message: input });  // Send via WS
      setMessages(prev => [...prev, { content: input, isUser: 1 }]);
      setInput('');
    }
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {messages.map((msg, idx) => <ChatBubble key={idx} message={msg} isUser={msg.is_user} />)}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-area">
        <input value={input} onChange={e => setInput(e.target.value)} placeholder="Message..." />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatWindow;