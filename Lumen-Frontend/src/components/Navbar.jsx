import React, { useContext, useState } from "react";
import Searchinput from "./Searchinput";
import { Button, Drawer } from "@mui/material";

import Logo from "./logo";
import DrawerList from "./DrawerList";
import { ThemeContext } from "../context/Themecontext";

const Navbar = () => {
  const [open, setOpen] = useState(false);
  const [user, setUser] = useState("");
  const [isActive, setIsActive] = useState("false");

  const { theme: mode, toggleTheme } = useContext(ThemeContext);

  const toggleDrawer = (newOpen) => () => {
    setOpen(newOpen);
  };
  const changeActive = () => {
    setIsActive(true);
  };
  const testDrawer = () => {
    user == "" && setUser("test");
  };

  return (
    <div>
      <div className="grid grid-cols-2 md:grid-cols-4  gap-4 items-center">
        <div className=" m-3 col-start-1 md:col-start-1">
          <Logo />
        </div>
        <div className="col-span-2 md:col-span-2 order-last md:order-none w-[97%] gap-0">
          <Searchinput />
        </div>
        <div className="justify-self-end col-start-2 md:col-start-4 m-3 p-3 font-bold cursor-pointer ">
          {user ? (
            <Button onClick={toggleDrawer(true)}>Profile</Button>
          ) : (
            <div>
              <Button onClick={toggleTheme} className="inline ">
                change theme
              </Button>
              <Button onClick={testDrawer} className="inline">
                Login
              </Button>
            </div>
          )}
          <div
            className={
              mode == "dark" ? "bg-black text-white" : "bg-white text-black"
            }
          >
            <Drawer anchor="right" open={open} onClose={toggleDrawer(false)}>
              <DrawerList
                user={user}
                isActive={isActive}
                toggleDrawer={toggleDrawer}
                changeActive={changeActive}
              />
            </Drawer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;

<nav className="w-full p-4 bg-white dark:bg-gray-900">
  <div className="grid grid-cols-2 md:grid-cols-3 gap-4 items-center">
    {/* Logo */}
    <div className="col-start-1 md:col-start-1">
      <img src="/logo.png" className="h-8" />
    </div>

    {/* Searchbar */}
    <div className="col-span-2 md:col-span-1 order-last md:order-none">
      <input
        type="text"
        placeholder="Search..."
        className="w-full px-4 py-2 rounded-xl bg-gray-100 dark:bg-gray-800"
      />
    </div>

    {/* Login/Profile */}
    <div className="justify-self-end col-start-2 md:col-start-3">
      <button className="px-4 py-2 rounded-xl bg-blue-500 text-white">
        Login
      </button>
    </div>
  </div>
</nav>;
