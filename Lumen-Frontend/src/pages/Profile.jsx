import { Button } from "@mui/material";
import React, { useState } from "react";
import Uploads from "./Uploads";

const Data = {
  Full_name: "John Doe",
  Username: "john_doe",
  Email: "john.doe@example.com",
  Mobile: "1234567890",
  City: "New York",
  Gender: "Male",
  Agree: true, // Boolean value for agreement to terms
  Profile_picture: "https://cdn-icons-png.flaticon.com/128/149/149071.png", // URL or file path
  Last_login: "2025-11-18T05:00:00Z", // Timestamp
  Contribution_count: 42, // Number of contributions
};
const Profile = ({ userData = Data }) => {
  const [disableEdit, setDisableEdit] = useState(true);

  const [profileData, setProfileData] = useState({
    Full_name: userData.Full_name,
    City: userData.City,
    Mobile: userData.Mobile,
  });
  const openPicture = (e) => {
    console.log("Profile picture clicked:", e.target.src);
    // Additional logic to handle picture click can be added here
  };

  const allowEdit = () => {
    setDisableEdit(false);
  };

  const saveChanges = () => {
    setDisableEdit(true);
  };
  return (
    <div>
      <div className="grid grid-cols-2 gap-2 w-full md:w-5/6 m-auto text-center my-7  border-b-2 border-gray-500 p-4">
        <h1 className="text-2xl font-bold m-auto">{userData.Username}</h1>
        <div
          className={
            disableEdit ? "w-max text-center m-auto md:mr-auto p-2" : "hidden"
          }
        >
          <Button variant="contained" color="primary" onClick={allowEdit}>
            Edit Profile
          </Button>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-2 w-full md:w-5/6 m-auto border-b-2 border-gray-500 pb-12 pt-5">
        <div className="columns-1 gap-3 w-1/2 m-auto md:mx-0 md:ml-auto">
          <img
            src={
              userData.Profile_picture
                ? userData.Profile_picture
                : "https://cdn-icons-png.flaticon.com/128/149/149071.png"
            }
            alt="profile"
            className="h-40 mt-5 w-max rounded-full ml-auto  mb-auto inline select-none border border-gray-300"
            onClick={openPicture}
          />
          <div className="w-max m-auto my-5">
            <Button variant="outlined" color="primary">
              Change
            </Button>
          </div>
        </div>
        <div className=" text-left m-auto col-start-1 gap-0 w-full p-2 md:col-span-2">
          <div className="flex flex-col md:w-max md:m-auto md:justify-start ">
            <div className="flex-col md:flex-row flex gap-1 md:gap-5">
              <span className="inline m-2 mr-auto text-2xl pt-2 text-gray-500 font-semibold">
                Full Name
              </span>{" "}
              <input
                type="text"
                value={profileData.Full_name}
                disabled={disableEdit}
                onChange={(e) =>
                  setProfileData((prev) => ({
                    ...prev,
                    [e.target.name]: e.target.value,
                  }))
                }
                name="Full_name"
                className="inline m-2 text-2xl font-semibold border p-2  pl-4"
              />
            </div>
            <div className="flex-col md:flex-row flex gap-1 md:gap-5">
              <span className="inline m-2 mr-auto text-2xl pt-2 text-gray-500 font-semibold">
                Email
              </span>{" "}
              <input
                type="text"
                value={userData.Email}
                disabled={true}
                className="inline m-2 text-2xl font-semibold border p-2  pl-4"
              />
            </div>
            <div className="flex-col md:flex-row flex gap-1 md:gap-5">
              <span className="inline m-2 mr-auto text-2xl pt-2 text-gray-500 font-semibold">
                City
              </span>{" "}
              <input
                type="text"
                value={profileData.City}
                disabled={disableEdit}
                onChange={(e) =>
                  setProfileData((prev) => ({
                    ...prev,
                    [e.target.name]: e.target.value,
                  }))
                }
                name="City"
                className="inline m-2 text-2xl font-semibold border p-2  pl-4"
              />
            </div>

            <div className="flex-col md:flex-row flex gap-1 md:gap-5">
              <span className="inline m-2 mr-auto text-2xl pt-2 text-gray-500 font-semibold ">
                Mobile
              </span>{" "}
              <input
                type="text"
                value={profileData.Mobile}
                disabled={disableEdit}
                onChange={(e) =>
                  setProfileData((prev) => ({
                    ...prev,
                    [e.target.name]: e.target.value,
                  }))
                }
                name="Mobile"
                className="inline m-2 text-2xl font-semibold border p-2  pl-4"
              />
            </div>
          </div>
        </div>
        <div
          className={
            disableEdit ? "hidden" : "md:col-span-3 m-auto w-max p-4 my-4"
          }
        >
          <Button
            variant="contained"
            color="primary"
            className="w-max"
            onClick={saveChanges}
          >
            Save Changes
          </Button>
        </div>
      </div>
      <p className="m-auto p-2 md:hidden  mt-5 font-medium">
        Update Your Password
      </p>
      <div className="flex flex-col gap-3 md:flex-row justify-center w-5/6 ml-10 md:mx-auto  mt-2">
        <input
          type="text"
          className="bg-white dark:bg-gray-700 dark:text-white dark:font-medium border border-black p-1.5 mx-3 text-black focus:outline-none rounded-sm"
        />
        <input
          type="text"
          className="bg-white dark:bg-gray-700 dark:text-white dark:font-medium border border-black p-1.5 mx-3 text-black focus:outline-none rounded-sm"
        />
        <div className="w-5/6 m-auto md:m-2 md:w-max md:h-full">
          <Button variant="contained" color="secondary">
            Change Password
          </Button>
        </div>
      </div>
      <Uploads />
    </div>
  );
};

export default Profile;
