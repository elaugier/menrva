import './App.css';

import NavBar, { MenuItem } from './components/NavBar';

import React from 'react';
import SiteTitle from './components/SiteTitle';

let menuItems: MenuItem[] = [
  { name: "Actualités", link: "" },
  { name: "Textes", link: "" },
  { name: "Evénementiels", link: "" },
  { name: "Jeux Littéraires", link: "" },
  { name: "Discussions", link: "" },
  { name: "Membres", link: "" },
]

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <SiteTitle name='La Passion des Poèmes'></SiteTitle>
        <NavBar name='Accueil' items={menuItems} />
      </header>
    </div>
  );
}

export default App;
