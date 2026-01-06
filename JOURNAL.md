## 3rd Jan 2026 

I decided on making a christmas conveyer belt to help Santa sort his Naughty and Nice presents ;) 

I wanted to make as much of the parts using a 3D printer as possible so I decided on making everything except the bearings using a printer. 

My plan is to use rollers with gears at either side I can use timing belts between rollers and only require one motor. Then I will use a TCRT5000 IR sensor that will detect how much of the IR light is reflected back. Coal will relfect very little back causing the rollers to spin clockwise. A gift wrapped present will reflect most of the light so rollers will spin anticlockwise. 

I began designing my own PCB using the ATMega328p so it would be compatible with arduino IDE allowing easy coding. This meant I need a header for the In System Programming AKA ISP so that I can use an ISP programmer to flash the program onto the Atmega328p. Then I used another header for connecting the TCRT5000 module to the PCB and also two headers for connecting the NEMA 17 motors. Then I settled on the TB6612FNG for its simplicity and also that fact that I hadn't used it before so I could learn something new. 

<img width="637" height="521" alt="image" src="https://github.com/user-attachments/assets/28ba87d7-06f8-49c6-8716-a0c87a3a7c5e" />

Once I finshed the schematic, I began populating my PCB. I tried very hard to only use one layer but I could not find a single way of making a complete PCB without jumpers. Eventually I surrendered and used two layers due to time constraints and exam pressure :(

<img width="887" height="871" alt="image" src="https://github.com/user-attachments/assets/ab5c5cbc-fd4e-46cd-bb01-a0e58082c772" />

<img width="522" height="540" alt="image" src="https://github.com/user-attachments/assets/0bb54ef9-efb8-443f-a522-b33a184420c9" />

Hours Spent: 3.5 Hrs

## 4th Jan 2026

I began creating my 3D model, starting with the rollers. The initial shape was easy but cretaing the teeth at the edges proved to be more difficult than expected. I discovered new features such as the circular pattern tool which really saved time and helped design the teeth accurately. I created the teeth to fit with a GT2 timing belt with a width of 6mm. I created the frame with a depth of 7mm to allow for the 608zz bearing to slot in place. I have used tight tolerances in order to make everything force fit instead of using screws ensuring most of the components are 3D printed. I also added a bit of Christmas colour to the rollers :) 

<img width="1255" height="456" alt="image" src="https://github.com/user-attachments/assets/d6873121-9eed-46e8-952a-74ab144c2224" />

<img width="995" height="543" alt="image" src="https://github.com/user-attachments/assets/e0e61bdb-b962-4ef6-8e99-1cc23ef7fd43" />

<img width="1200" height="586" alt="image" src="https://github.com/user-attachments/assets/6ff4afbc-c4b1-40c0-8dfd-0e6eea3414d8" />

Hours Spent: 2Hrs
