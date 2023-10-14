import React, {useState} from 'react';
import Modal from "./Modal.jsx";
import {register} from "../utils/auth.js";

function SignUpForm() {
    const [name, setName] = useState('')
    const [lastName, setLastName] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [cPassword, setCPassword] = useState('')

    const signUp = e => {
        e.preventDefault()
        register(email, password, name, lastName)
            .then(res => console.log(res.data.data))
            .catch(err => console.error(err))
    }

    return (
        <Modal>
            <h1 className="text-3xl text-center font-semibold">Registration</h1>
            <br/>
            <form
                className="space-y-4"
                onSubmit={e => signUp(e)}

            >
                <div>
                    <input
                        type="text" placeholder="Name"
                        className="w-full input input-bordered input-success"
                        onChange={e => setName(e.target.value)}
                        value={name}
                    />
                </div>
                <div>
                    <input
                        type="text" placeholder="Last Name"
                        className="w-full input input-bordered input-success"
                        onChange={e => setLastName(e.target.value)}
                        value={lastName}
                    />
                </div>
                <div>

                    <input
                        type="text" placeholder="Email Address"
                        className="w-full input input-bordered input-success"
                        onChange={e => setEmail(e.target.value)}
                        value={email}
                    />
                </div>
                <div>

                    <input
                        type="password" placeholder="Enter Password"
                        className="w-full input input-bordered input-success"
                        onChange={e => setPassword(e.target.value)}
                        value={password}
                    />
                </div>
                <div>

                    <input
                        type="password" placeholder="Confirm Password"
                        className="w-full input input-bordered input-success"
                        onChange={e => setCPassword(e.target.value)}
                        value={cPassword}
                    />
                </div>
                <div>
                    <button
                        className="btn btn-block btn-success text-white"
                    >Sign Up
                    </button>
                </div>
                <h1 className="text-center">Already have an account ?
                    <a href="#" className="text-blue-600 hover:text-blue-800 hover:underline">Login</a>
                </h1>
            </form>
        </Modal>
    );
}

export default SignUpForm;