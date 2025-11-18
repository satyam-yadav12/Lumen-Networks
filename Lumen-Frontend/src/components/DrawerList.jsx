import React from "react";
import { Link, Navigate } from "react-router-dom";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";

const DrawerList = ({ user, isActive, toggleDrawer, changeActive }) => {
  return (
    <Box sx={{ width: 250 }} role="presentation">
      <div className="ml-auto m-3 p-3 font-bold  mt-[50px] w-full flex ">
        <p className="inline mr-auto">{user ? user : "Login / Register"}</p>
        <span
          className={`ml-auto mr-3 px-3 cursor-pointer rotate-element ${
            isActive ? "active-state" : ""
          }`}
          onClick={toggleDrawer(false)}
        >
          X
        </span>
      </div>
      <List>
        {["Profile", "Collection", "Uploads", "Upload Image"].map(
          (text, index) => (
            <Link to={"/" + text.toLowerCase().replace(" ", "-")}>
              <ListItem key={text} onClick={toggleDrawer(false)} disablePadding>
                <ListItemButton>
                  {" "}
                  <ListItemText primary={text} />
                </ListItemButton>
              </ListItem>
            </Link>
          )
        )}
      </List>
      <Divider />
      <List>
        {["Change Theme", "Log out"].map((text, index) => (
          <ListItem key={text} disablePadding>
            <ListItemButton>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default DrawerList;
