import React, { useState } from "react";
import Popup from "./components/Popup";

const data = {
  sender_gst: "ABCDEFGHIJKLMNOP",
  sender_mobile: "9810833220",
  from_addr: {
    addr: "Hamilton, New York",
    company_name: "Python Tip",
    state_code: 9,
    gst: "EJOTYKSHVFENJYU",
  },
  transport_details: {
    transport: "",
    pOrderNo: "",
    "numberOfPkgs.": "",
    supplyDateTime: "",
    supplyPlace: "",
    vehicleNumber: "",
    grNumber: "",
  },
  invoice_number: 156,
  items: [
    {
      index: 0,
      hsn: 3924,
      qty: 234,
      rate: 180.0,
      title: "website design",
    },
    {
      index: 1,
      hsn: 3924,
      qty: 24,
      rate: 180.0,
      title: "Water jug",
    },
  ],
  amountInWords:
    "Twelve Crore Thirty Four Lakh Fifty Six Thousand Seven Hundred Ninety Nine only",
  discount: 0,
  extraCost: 0,
  totalBeforeTax: 20000,
  cgst: 0,
  cgstAmount: 0,
  sgst: 0,
  sgstAmount: 0,
  igst: 18,
  igstAmount: 360,
  netAmount: 2360,
};

function App() {
  const [isOpen, setIsOpen] = useState(false);

  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  const handleDownload = () => {
    window.open("http://192.168.43.210:5000/get-pdf/invoice4.pdf");
    setIsOpen(false);
  };
  const handleClick = () => {
    fetch("http://192.168.43.210:5000/", {
      method: "POST",
      body: JSON.stringify(data),
      headers: { "Content-type": "application/json" },
    })
      // Handle success
      .then((response) => response.json()) // convert to json
      .then((response) => console.log(response))
      .then(togglePopup) //print data to console
      .catch((err) => console.log("Request Failed", err)); // Catch errors
  };
  return (
    <div className="App">
      <button onClick={handleClick}> Press this to start generating</button>
      {isOpen && (
        <Popup handleClick={handleDownload} handleClose={togglePopup} />
      )}
    </div>
  );
}

export default App;
