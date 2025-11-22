import { Button } from "@mui/material";
import React from "react";
import { Link } from "react-router-dom";

const Login = () => {
  const handleLogin = () => {
    console.log("login clicked");
  };
  return (
    <div className="relative w-full  overflow-hidden">
      <div className="flex flex-row w-screen h-[80vh] overflow-hidden">
        <div className="bg-white dark:bg-gray-300 w-full"></div>
        <div className="bg-[#00A2CA] dark:bg-[#222224] w-full"></div>
      </div>
      <div className="top-[50%] left-[50%] transform -translate-x-1/2 -translate-y-1/2 absolute grid grid-cols-1 md:grid-cols-4 text-left gap-6 w-screen">
        <div className="hidden md:block col-start-1 bg-[url(/theme-3.svg.png)] bg-no-repeat bg-center bg-contain mx-4 px-4 w-full "></div>
        {/* Login form */}
        <div className="w-5/6 m-auto p-10 bg-white dark:bg-[#222224] h-full border border-white shadow-black drop-shadow-2xl  rounded-3xl col-start-1 md:col-span-2 md:col-start-2 flex flex-col justify-start ">
          <h1 className="text-left font-bold text-2xl my-3 mt-1 ">Login</h1>
          <div className="text-left ">
            <label htmlFor="username" className="text-left my-2 py-2">
              <span className="py-2 my-2 ">Enter Email</span>
              <input
                type="text"
                className="rounded-sm w-full m-auto border p-2 mb-2 border-gray-200 outline-1 dark:hover:outline-whitehover:outline-[#00A2CA] focus:outline-[#00A2CA]"
                placeholder="Enter a Valid Email"
              />
            </label>
          </div>
          <div className="text-left my-2 py-2">
            <label htmlFor="password" className="text-left">
              <span className="py-2 my-2 ">Enter Password</span>
              <input
                type="text"
                className="rounded-sm w-full m-auto border p-2 mb-2  border-gray-200 outline-1 dark:hover:outline-white hover:outline-[#00A2CA] focus:outline-[#00A2CA]"
                placeholder="Enter your Password"
              />
            </label>
          </div>
          <div className="flex flex-col justify-center bg-[#00A2CA] dark:bg-white  dark:text-black text-white rounded-sm my-2  font-semibold">
            <Button onClick={handleLogin} color="inherit">
              Login
            </Button>
          </div>
          <p className="font-light text-center ">
            Not registered yet?{" "}
            <Link to="/register">
              <span className="text-blue-500 font-normal ">Register</span>
            </Link>{" "}
            here
          </p>
        </div>
        <div className=" hidden md:block col-start-4 bg-[url(/common.svg.png)] bg-no-repeat bg-center bg-cover ml-auto px-4 w-full "></div>
      </div>
    </div>
  );
};

export default Login;
