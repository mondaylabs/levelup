import React from 'react';

function Navbar() {
    return (
        <div className="navbar">
            <div className="navbar-start">
                <a className="btn btn-ghost normal-case text-xl">Level Up</a>
            </div>
            <div className="navbar-end">
                <a className="btn btn-success text-white">Log in</a>
            </div>
        </div>
    );
}

export default Navbar;