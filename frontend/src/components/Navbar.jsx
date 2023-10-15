import React from 'react';

function Navbar() {
    return (
        <div className="navbar">
            <div className="navbar-start">
                <a className="btn btn-ghost normal-case text-xl">Level Up</a>
            </div>
            <div className="navbar-end">
                <a
                    onClick={() => document.getElementById('my_modal_3').showModal()}
                    className="btn btn-success text-white"

                >Sign Up</a>
            </div>
        </div>
    );
}

export default Navbar;