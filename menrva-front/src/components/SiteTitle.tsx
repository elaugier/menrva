import React, { Component } from 'react';

type SiteTitleProps = {
    name: string
}

export default class SiteTitle extends Component<SiteTitleProps> {
    static defaultProps = {
        name: 'Site title'
    }

    render() {
        return <h1>{this.props.name}</h1>
    }

}