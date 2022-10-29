import './NavBar.css'

import React, { Component } from 'react';

export type MenuItem = {
    name: string,
    link: string
}

type NavBarProps = {
    name: string,
    items: MenuItem[]
}

export default class NavBar extends Component<NavBarProps> {
    static defaultProps = {
        name: 'Accueil',
        items: []
    }

    render() {
        return <ul className='App-Navbar'>
            <li><a href='/'>{this.props.name}</a></li>
            {this.props.items.map((item, i) => <li><a href={item.link}>{item.name}</a></li>)}
        </ul>
    }

}