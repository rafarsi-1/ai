import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import './styles.css';

const App = () => {
  const [selectedCharacter, setSelectedCharacter] = useState(null);

  return (
    <div className="app">
      <Sidebar onSelectCharacter={setSelectedCharacter} />
      {selectedCharacter ? <ChatWindow characterId={selectedCharacter} /> : <div>Select a character to chat</div>}
    </div>
  );
};

export default App;