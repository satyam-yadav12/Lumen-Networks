import React from "react";

const Logo = () => {
  return (
    <div className="flex flex-row cursor-context-menu select-none">
      <img src="src/assets/logo.png" alt="Lumen" className="inline p-1 h-13" />
      <div className="inline p-1">
        <p className="font-extrabold mb-0">LUMEN</p>
        <p className="font-bold mb-0">Networks</p>
      </div>
    </div>
  );
};

export default Logo;
