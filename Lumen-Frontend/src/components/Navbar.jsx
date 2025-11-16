import React, { useState } from "react";
import Searchinput from "./Searchinput";
import { Button, Drawer } from "@mui/material";

import Box from "@mui/material/Box";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";

const Navbar = () => {
  const [open, setOpen] = useState(false);
  const [user, setUser] = useState("");
  const toggleDrawer = (newOpen) => () => {
    setOpen(newOpen);
  };

  const DrawerList = (
    <Box sx={{ width: 250 }} role="presentation">
      <div
        className="ml-auto m-3 p-3 font-bold cursor-pointer mt-[50px] w-full"
        onClick={toggleDrawer(false)}
      >
        close sidebar
      </div>
      <List>
        {["Profile", "Collection", "Uploads", "Upload New Image"].map(
          (text, index) => (
            <ListItem key={text} disablePadding>
              <ListItemButton>
                <ListItemText primary={text} />
              </ListItemButton>
            </ListItem>
          )
        )}
      </List>
      <Divider />
      <List>
        {["Log out"].map((text, index) => (
          <ListItem key={text} disablePadding>
            <ListItemButton>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );
  return (
    <div>
      <div className="flex justify-around">
        <div className="mr-auto m-3 ">
          <p className="font-extrabold mb-0">LUMEN</p>
          <p className="font-bold mb-0">Networks</p>
        </div>
        <div className="w-1/2">
          <Searchinput />
        </div>
        <div className="ml-auto m-3 p-3 font-bold cursor-pointer ">
          {user ? (
            <Button onClick={toggleDrawer(true)}>Profile</Button>
          ) : (
            <Button>Login / Register</Button>
          )}
          <Drawer anchor="right" open={open} onClose={toggleDrawer(false)}>
            {DrawerList}
          </Drawer>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
