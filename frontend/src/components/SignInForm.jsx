import React, {useState} from 'react';
import Modal from "./Modal.jsx";

function SignInForm() {
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    return (
        <Modal>
            <h1 className="text-3xl text-center font-semibold">Registration</h1>
            <br/>
            <form className="space-y-4">
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
                <h1 className="text-center">Already have an account ?
                    <a href="#" className="text-blue-600 hover:text-blue-800 hover:underline">Login</a>
                </h1>
            </form>
        </Modal>
    );
}

export default SignInForm;