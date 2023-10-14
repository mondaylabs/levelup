import React from 'react';
import Modal from "./Modal.jsx";

function SignInForm() {
    return (
        <Modal>
            <h1 className="text-3xl text-center font-semibold">Registration</h1>
            <br/>
            <form className="space-y-4">
                <div>
                    <input type="text" placeholder="Name"
                           className="w-full input input-bordered input-success"/>
                </div>
                <div>

                    <input type="text" placeholder="Email Address"
                           className="w-full input input-bordered input-success"/>
                </div>
                <div>

                    <input type="password" placeholder="Enter Password"
                           className="w-full input input-bordered input-success"/>
                </div>
                <div>

                    <input type="password" placeholder="Confirm Password"
                           className="w-full input input-bordered input-success"/>
                </div>
                <div>
                    <button className="btn btn-block btn-success text-white">Sign Up</button>
                </div>
                <h1 className="text-center">Already have an account ?
                    <a href="#" className="text-blue-600 hover:text-blue-800 hover:underline">Login</a>
                </h1>
            </form>
        </Modal>
    );
}

export default SignInForm;