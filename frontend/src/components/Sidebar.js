import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Sidebar = ({ onSelectCharacter }) => {
  const [characters, setCharacters] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/characters').then(res => setCharacters(res.data));
  }, []);

  return (
    <div className="sidebar">
      <button>Create</button>
      <div>Discover</div>
      <input type="text" placeholder="Search for Characters" value={search} onChange={e => setSearch(e.target.value)} />
      <h3>Recent</h3>
      {characters.filter(c => c.name.toLowerCase().includes(search.toLowerCase())).map(char => (
        <div key={char.id} onClick={() => onSelectCharacter(char.id)} style={{ cursor: 'pointer', margin: '10px 0' }}>
          <img src={char.icon || 'default-icon.png'} alt="" style={{ width: 40, borderRadius: '50%' }} />
          {char.name}
        </div>
      ))}
    </div>
  );
};

export default Sidebar;