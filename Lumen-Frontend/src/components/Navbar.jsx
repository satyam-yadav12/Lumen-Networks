import React, { useState } from "react";
import Searchinput from "./Searchinput";
import { Button, Drawer } from "@mui/material";

import Logo from "./logo";
import DrawerList from "./DrawerList";

const Navbar = () => {
  const [open, setOpen] = useState(false);
  const [user, setUser] = useState("");
  const [isActive, setIsActive] = useState("false");
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
      <div className="flex justify-around">
        <div className="mr-auto m-3 ">
          <Logo />
        </div>
        <div className="w-1/2">
          <Searchinput />
        </div>
        <div className="ml-auto m-3 p-3 font-bold cursor-pointer ">
          {user ? (
            <Button onClick={toggleDrawer(true)}>Profile</Button>
          ) : (
            <Button onClick={testDrawer}>Login</Button>
          )}
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
  );
};

export default Navbar;
