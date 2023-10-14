import React from 'react';

function Sidebar({children, bg}) {
    return (
        <div className={`w-[20%] ${bg} min-h-[100vh] shadow-xl
             flex gap-[24px] items-center p-[15px] py-[10px] flex-col rounded-se-[100px] fixed z-[99]`}>
            {children}
        </div>

    );
}

export default Sidebar;