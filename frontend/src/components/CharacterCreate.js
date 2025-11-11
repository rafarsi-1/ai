import React, { useState } from 'react';
import axios from 'axios';

const CharacterCreate = ({ onCreate }) => {
  const [name, setName] = useState('');
  const [desc, setDesc] = useState('');

  const create = () => {
    axios.post('http://localhost:8000/characters', { name, description: desc }).then(res => onCreate(res.data));
  };

  return (
    <div>
      <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
      <textarea placeholder="Description (personality, greeting)" value={desc} onChange={e => setDesc(e.target.value)} />
      <button onClick={create}>Create Character</button>
    </div>
  );
};

export default CharacterCreate;