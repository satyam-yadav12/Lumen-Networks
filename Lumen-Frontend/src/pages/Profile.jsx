import { Button } from "@mui/material";
import React from "react";

const Profile = ({ Data }) => {
  const userData = [
    {
      Full_name: "John Doe",
      Email: "john.doe@example.com",
      Mobile: "1234567890",
      City: "New York",
      Gender: "Male",
      Agree: true, // Boolean value for agreement to terms
      Profile_picture: "https://cdn-icons-png.flaticon.com/128/149/149071.png", // URL or file path
      Last_login: "2025-11-18T05:00:00Z", // Timestamp
      Contribution_count: 42, // Number of contributions
    },
  ];

  const openPicture = (e) => {
    console.log("Profile picture clicked:", e.target.src);
    // Additional logic to handle picture click can be added here
  };
  return (
    <div>
      {userData.map((val) => {
        return (
          <div key={val.Email} className="text-start p-3 m-3">
            <img
              src={
                val.Profile_picture
                  ? val.Profile_picture
                  : "https://cdn-icons-png.flaticon.com/128/149/149071.png"
              }
              alt="profile"
              className="h-12 w-max rounded-full m-3 mb-1 inline select-none border-1 border-gray-300"
              onClick={openPicture}
            />
            <h1 className="inline m-3 text-2xl font-medium ml-0 my-0">
              {" "}
              {val.Full_name}
            </h1>
            <div className="ml-14 p-3 grid grid-cols-2 grid-rows-2 gap-0 text-start w-1/2">
              <p className="inline mx-2">
                <strong>Email:</strong> {val.Email}
              </p>
              <p className="inline mx-2">
                <strong>Mobile:</strong> {val.Mobile}
              </p>
              <p className="inline mx-2">
                <strong>City:</strong> {val.City}
              </p>
              <p className="inline mx-2">
                <strong>Gender:</strong> {val.Gender}
              </p>
            </div>
            <div className="ml-14 p-3 columns-2"></div>
          </div>
        );
      })}

      <div className="m-3 flex flex-col justify-start w-max ml-24">
        <Button variant="contained" color="primary">
          Edit Profile
        </Button>
      </div>
    </div>
  );
};

export default Profile;
