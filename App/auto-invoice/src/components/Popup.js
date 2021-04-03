import React from "react";
import styled from "styled-components";

function Popup(props) {
  return (
    <div>
      <PopupBox>
        <Box>
          <Close onClick={props.handleClose}>x</Close>
          Invoice Generated. Click to Download!
          <br />
          <br />
          <button onClick={props.handleClick}>Downlaod</button>
        </Box>
      </PopupBox>
    </div>
  );
}

const PopupBox = styled.div`
  position: fixed;
  background: #00000050;
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
`;
const Box = styled.div`
  position: relative;
  width: 20vw;
  text-align: center;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  height: auto;
  max-height: 70vh;
  margin-top: calc(100vh - 85vh - 20px);
  background: #fff;
  border-radius: 4px;
  padding: 20px;
  border: 1px solid #999;
  overflow: auto;
  @media (max-width: 800px) {
    width: 30vw;
  }
`;
const Close = styled.span`
  content: "x";
  cursor: pointer;
  position: fixed;
  right: calc(40% - 30px);
  top: calc(100vh - 85vh - 33px);
  background: #ededed;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  line-height: 20px;
  text-align: center;
  border: 1px solid #999;
  font-size: 20px;
`;
export default Popup;
