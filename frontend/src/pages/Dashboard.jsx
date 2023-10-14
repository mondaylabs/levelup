import React from 'react';
import Sidebar from "../components/Sidebar.jsx";
import {Chart as ChartJS, Filler, Legend, LineElement, PointElement, RadialLinearScale, Tooltip,} from 'chart.js';
import {Radar} from 'react-chartjs-2';


ChartJS.register(
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip,
    Legend
);
export const data = {
    labels: ['Thing 1', 'Thing 2', 'Thing 3', 'Thing 4', 'Thing 5', 'Thing 6'],
    datasets: [
        {
            label: '# of Votes',
            data: [2, 9, 3, 5, 2, 3],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
        },
    ],
};

function Dashboard() {
    return (
        <div className="flex">
            <Sidebar>
                <div className="py-10">
                    <h1 className="text-3xl font-bold ">Level Up</h1>
                </div>
                <ul className="menu w-100 rounded-box text-xl">
                    <li><a>DashBoard</a></li>
                    <li><a>Item 2</a></li>
                    <li><a>Item 3</a></li>
                </ul>
            </Sidebar>
            <div className="w-[80%] ">
                <div className="navbar bg-base-100 flex-row-reverse">
                    <div className="flex-none gap-2 ">
                        <div className="form-control">
                            <input type="text" placeholder="Search" className="input
                            rounded-3xl input-bordered w-24 md:w-auto focus:outline-0"/>
                        </div>
                        <div className="dropdown dropdown-end">
                            <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
                                <div className="w-10 rounded-full">
                                    <img src="https://avatars.githubusercontent.com/u/99078318?v=4"/>
                                </div>
                            </label>
                            <ul tabIndex={0}
                                className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                                <li>
                                    <a className="justify-between">
                                        Profile
                                        <span className="badge">New</span>
                                    </a>
                                </li>
                                <li><a>Settings</a></li>
                                <li><a>Logout</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="p-10 flex flex-col gap-10">
                    <div className="flex justify-between   gap-3 items-start ">
                        <div className="card w-1/4 bg-base-100 shadow-xl">
                            <div className="px-5 pt-5">
                                <h1 className="card-title">Diogram 1</h1>
                            </div>
                            <figure>
                                <Radar data={data}/>;
                            </figure>
                            <div className="px-5 py-5">
                                <h2 className="card-title">Shoes!</h2>
                                <p>If a dog chews shoes whose shoes does he choose?</p>

                            </div>
                        </div>
                        <div className="card w-1/4 bg-base-100 shadow-xl">
                            <div className="px-5 pt-5">
                                <h1 className="card-title">Diogram 1</h1>
                            </div>
                            <figure>
                                <Radar data={data}/>;
                            </figure>
                            <div className="px-5 py-5">
                                <h2 className="card-title">Shoes!</h2>
                                <p>If a dog chews shoes whose shoes does he choose?</p>

                            </div>
                        </div>
                        <div className="card w-1/4 bg-base-100 shadow-xl">
                            <div className="px-5 pt-5">
                                <h1 className="card-title">Diogram 1</h1>
                            </div>
                            <figure>
                                <Radar data={data}/>;
                            </figure>
                            <div className="px-5 py-5">
                                <h2 className="card-title">Shoes!</h2>
                                <p>If a dog chews shoes whose shoes does he choose?</p>

                            </div>
                        </div>
                        <div className="card w-1/4 bg-base-100 shadow-xl">
                            <div className="px-5 pt-5">
                                <h1 className="card-title">Diogram 1</h1>
                            </div>
                            <figure>
                                <Radar data={data}/>;
                            </figure>
                            <div className="px-5 py-5">
                                <h2 className="card-title">Shoes!</h2>
                                <p>If a dog chews shoes whose shoes does he choose?</p>

                            </div>
                        </div>


                    </div>
                    <div className="flex justify-between">
                        <div className="w-1/2">
                            <div className="card bg-base-100 shadow-xl">
                                <div className="px-5 pt-5">
                                    <h1 className="card-title">Diogram 1</h1>
                                </div>
                                <figure>
                                    <Radar data={data}/>
                                </figure>
                                <div className="px-5 py-5">
                                    <h2 className="card-title">Shoes!</h2>
                                    <p>If a dog chews shoes whose shoes does he choose?</p>

                                </div>
                            </div>
                        </div>
                          <div className="w-1/2">
                            <div className="card bg-base-100 shadow-xl">
                                <div className="px-5 pt-5">
                                    <h1 className="card-title">Diogram 1</h1>
                                </div>
                                <figure>
                                    <Radar data={data}/>
                                </figure>
                                <div className="px-5 py-5">
                                    <h2 className="card-title">Shoes!</h2>
                                    <p>If a dog chews shoes whose shoes does he choose?</p>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    );
}

export default Dashboard;