import React from 'react';

function Sidebar({children}) {
    return (
        <div className="w-[20%] bg-gray-50  min-h-[100vh] shadow-xl
             flex gap-[24px] items-center p-[15px] py-[10px] flex-col rounded-se-[100px]">
            {children}
        </div>

    );
}

export default Sidebar;