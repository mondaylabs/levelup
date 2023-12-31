import React from 'react';
import Sidebar from "../components/Sidebar.jsx";
import {Chart as ChartJS, Filler, Legend, LineElement, PointElement, RadialLinearScale, Tooltip,} from 'chart.js';
import {Radar} from 'react-chartjs-2';
import {FaBeer} from "react-icons/fa";
import {RxDashboard} from "react-icons/rx";


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
            <Sidebar bg={`bg-[#44ad4e] text-white`}>
                <h1 className='font-bold text-[48px] mt-[32px]'>Leveup</h1>
                <div className="flex flex-col gap-[12px]">
                    <button
                        className='flex items-center px-[12px] py-[4px] rounded-[8px] gap-[8px] text-[20px] hover:bg-[#3d3d3d] transition duration-150 ease-out hover:ease-in'>
                        <RxDashboard className='text-[24px]'/>
                        Dashboard
                    </button>
                    <button
                        className='flex items-center px-[12px] py-[4px] rounded-[8px] gap-[8px] text-[20px] hover:bg-[#3d3d3d] transition duration-150 ease-out hover:ease-in'>
                        <RxDashboard className='text-[24px]'/>
                        Settings
                    </button>
                    <button
                        className='flex items-center px-[12px] py-[4px] rounded-[8px] gap-[8px] text-[20px] hover:bg-[#3d3d3d] transition duration-150 ease-out hover:ease-in'>
                        <RxDashboard className='text-[24px]'/>
                        Log out
                    </button>
                </div>
            </Sidebar>
            <div className="w-[80%] ml-[20%] p-[24px] ">
                <div className="flex justify-between ">
                    <h1 className='text-[32px] font-bold text-[#44AD4E]'>Dashboard</h1>
                    <div className="form-control w-[30%]">
                        <input type="text" placeholder="Search" className="input
                            rounded-3xl input-bordered w-24 md:w-auto focus:outline-0"/>
                    </div>
                    <div className="flex items-center gap-[12px]">
                        <h1 className='text-[20px] font-bold text-[#44ad4e]'>Shakhboz</h1>
                        <div className="dropdown dropdown-end">
                            <div tabIndex={0} className="btn btn-ghost btn-circle w-[50px]">
                                <img className='rounded-[100%]'
                                     src="https://avatars.githubusercontent.com/u/99078318?v=4"/>
                            </div>
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

                <div className="flex flex-col gap-[24px]">
                    <div className="flex justify-between   gap-3 items-start ">
                        <div className="card w-[50%] bg-base-100 shadow-xl p-[24px]">
                            <h1>Heloo</h1>
                            <figure>
                                <Radar data={data}/>
                            </figure>
                        </div>
                        <div className="card w-[50%] bg-base-100 shadow-xl p-[24px]">
                            <h1>Heloo</h1>
                            <figure>
                                <Radar data={data}/>
                            </figure>
                        </div>
                    </div>
                    <h1 className='text-[32px] font-bold text-[#44AD4E]'>Recommendation curses</h1>
                    <div className="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
                        <div className="inline-block min-w-full shadow-md rounded-lg overflow-hidden">
                            <table className="min-w-full leading-normal">
                                <thead>
                                <tr>
                                    <th
                                        className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider"
                                    >
                                        Тема
                                    </th>
                                    <th
                                        className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider"
                                    >
                                        Status
                                    </th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr>
                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                        <div className="flex">
                                            <div className="ml-3">
                                                <p className="text-gray-900 whitespace-no-wrap">
                                                    Введение в React.js
                                                </p>
                                            </div>
                                        </div>
                                    </td>

                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                <span
                    className="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight"
                >
                  <span
                      aria-hidden
                      className="absolute inset-0 bg-green-200 opacity-50 rounded-full"
                  ></span>
                  <span className="relative">Активный</span>
                </span>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
