import React from 'react';

const ChatBubble = ({ message, isUser }) => (
  <div style={{ display: 'flex', justifyContent: isUser ? 'flex-end' : 'flex-start', marginBottom: 10 }}>
    <div style={{
      padding: 10,
      borderRadius: 20,
      maxWidth: '60%',
      background: isUser ? '#f50' : '#333',
      color: '#fff'
    }}>
      {message.content}
    </div>
  </div>
);

export default ChatBubble;