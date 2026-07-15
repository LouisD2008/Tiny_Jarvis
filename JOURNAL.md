# TINY_JARVIS JOURNAL

## Table of contents:
 - [June 15](#june-15-started-prototyping) : 3 hours

## June 15: Started prototyping + visuals

<table border="0">
  <tr>
    <td valign="top">
      <img src="https://cdn.hackclub.com/019f6692-acd1-7dd8-9a5f-7f35852d8203/paste-1784132312883.png" width="900px">
    </td>
    <td valign="top">
      <p>I received all the materials I needed to start prototyping:</p>
      <ul>
        <li>1x Pack of Female-to-Female (F-F) Jumper Wires (40pcs ribbon)</li>
        <li>1x Pack of Female-to-Male (F-M) Jumper Wires (40pcs ribbon)</li>
        <li>1.3" OLED</li>
        <li>2x MAX98357A I2S Amps: for transforming digital signal into analog for speaker (=amplifiers)</li>
        <li>Rotary Encoder Module 5 pin version (for volume)</li>
        <li>A LOT of Push buttons (way too many, I only need two)</li>
        <li>2x 3W Speaker</li>
        <li>Medium breadboard</li>
        <li>Cheap USB mic</li>
      </ul>
    </td>
  </tr>
</table>

The first difficulty was met when connecting all these components together during prototyping. The rotary encoder and OLED did not give me any trouble, I just had to connect them to the right GPIO pins on the pi.(The screen looks weird bc i wasnt using Luma) 


<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f6693-5e78-711d-9f17-6957b8e75dbd/paste-1784132358841.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f6693-8d02-7f43-a5b6-faee9ba69a32/paste-1784132368397.png" width="150">
    </td>
  </tr>
</table>

However the soldering did not go as well; this was my first time soldering electronic components and it did not look good. 😅 I didn't have the right type of soldering iron to be faire, so I bought a new one (industral soldering iron).

<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f6680-1b29-70d0-9e6c-37d84d8eb0f0/prototyping.jpg" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f669f-14b5-7fe3-b0c1-0f6062149d63/paste-1784133128324.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f669f-b6bc-7756-80f7-4c381a12ca55/paste-1784133162524.png" width="150">
    </td>
  </tr>
</table>

As a matter of fact, the speakers did not work, as the connection to the amp was too poor. So i decided to just connect the rpi5 via bluetooth to a small JBL speaker.

But in a PCB, this would be much different since the connection would be direct, so I will implement the amps + speakers in the PCB later on.


<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f66a5-508a-77c7-9c2a-b47e20f953b3/paste-1784133537475.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66a5-96e5-78f9-a60f-08bad59182ec/paste-1784133555530.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66a8-8844-7280-8244-3d438b5111eb/paste-1784133748390.png" width="150">
    </td>
    <td>
    <img src="https://cdn.hackclub.com/019f66a8-ecdf-7716-a163-5b531a83cf56/paste-1784133774152.png">
  </tr>
</table>
(These are animated btw, just can't render them in a JOURNAL.md)


**Time spent this session: 3 hours (2 for prototyping and 1 for the oled screen animations)**