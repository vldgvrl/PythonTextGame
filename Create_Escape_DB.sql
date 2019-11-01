DROP DATABASE IF EXISTS escape_text_adventure;

CREATE DATABASE escape_text_adventure;

USE escape_text_adventure;

CREATE TABLE Room
(
  Room_ID INT NOT NULL,
  Name Varchar(40) NOT NULL,
  Room_Description Varchar(500) NOT NULL,
  Visited Bool,
  Map_Coordinates varchar(40),
  PRIMARY KEY (Room_ID)
);

CREATE TABLE Item
(
  Item_ID INT NOT NULL AUTO_INCREMENT,
  Name Varchar(40) NOT NULL,
  Technical_Name Varchar(40) NOT NULL,
  Description Varchar(300) NOT NULL,
  Room_ID INT,
  Available bool,
  Takeable bool,
  Carried Bool,
  PRIMARY KEY (Item_ID),
  FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
);

CREATE TABLE NPC
(
  NPC_ID INT NOT NULL,
  Name Varchar(40) NOT NULL,
  Speech Varchar(255) NOT NULL,
  Room_ID INT NOT NULL,
  PRIMARY KEY (NPC_ID),
  FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
);

CREATE TABLE Access
(
  Access_Source_ID INT NOT NULL,
  Direction Varchar(10) NOT NULL,
  Access_Target_ID INT NOT NULL,
  Locked BOOL,
  Description Varchar(100),
  PRIMARY KEY (Access_Source_ID, Direction),
  FOREIGN KEY (Access_Source_ID) REFERENCES Room(Room_ID),
  FOREIGN KEY (Access_Target_ID) REFERENCES Room(Room_ID)
);

#INSERTIT TÄHÄN
INSERT INTO Room (Room_ID, Name, Room_Description, Visited, Map_Coordinates) VALUES
(1, '???', 'You are in a room, there is a computer on the table. There is a door to the east with a keypad next to it.', True, '0,30,60,90'),
(2, 'Boiler room', 'You are in a boiler room, it´s quite hot in here. There is a spiral staircase leading up.', False, '60,30,120,90'),
(3, 'Lobby', 'You are in the Lobby, there is a spiral staircase leading up and down, there are also doors to the east, west and south.', False, '60,60,150,120'),
(4, 'West Hallway', 'You are in a hallway there are doors to the east, south, west and north east.', False, '30,30,60,120'),
(5, 'Dining hall', 'You are in the dining hall, there is a large table with six chairs around it, there are doors leading south west and south east. ', False, '60,0,150,60'),
(6, 'Livingroom', 'You are in the livingroom, there is a door leading north.', False, '0,120,60,180'),
(7, 'Kitchen', 'You are in the kitchen, there are doors to the north, east and south.', False, '0,60,30,90'),
(8, 'Pantry', 'You are in a pantry, there is a door leading south.', False, '0,30,30,60'),
(9, 'Supply Closet', 'You are in a supply closet, there is a door leading north.', False, '0,90,30,120'),
(10, 'East Hallway', 'You are in a hallway, there are doors leading north west, east, south and west.', False, '150,30,180,120'),
(11, 'Garage', 'You are in the garage, there is a car in here. There is a door to the north.', False, '150,120,210,180'),
(12, 'Recreation room', 'You are in the recreation room, there is a pool table in the middle and a dart board on the wall. There are doors leading south and east.', False, '180,30,210,90'),
(13, 'Bathroom', 'You are in the bathroom, there is a door leading north.', False, '180,90,210,120'),
(14, 'Front yard', 'Aagh, the light is blinding outside! Hey, I escaped! FREEDOM!', False, '60,120,150,150'),
(15, '2nd floor Hallway', 'You are in a hallway, there are spiral stairs leading down, and doors to the east, south and west.', False, '60,0,150,60'),
(16, 'Master Bedroom', 'You are in a bedroom. There is grand twin bed and a cupboard on the south wall. You hear faint static noise coming from somewhere. There is a door to the east', False, '0,0,60,30'),
(17, 'Hidden room', 'You are in a hidden room, looks like a man-cave. There is a doll sitting on the sofa. TV is on but it is only showing static. There is a door to the north.', False, '0,30,60,60'),
(18, 'Library', 'You are in a library, the bookcases are marked with letters A-G, and shelves are all numbered 1-20 in every case. There is a door leading east.', False, '150,0,210,90'),
(19, 'Greenhouse', 'You are in the greenhouse, there is a door leading east.', False, '0,60,60,120'),
(20, 'Supply room', 'You are in a supply room, there are doors leading north and west', False, '60,60,150,90');

INSERT INTO Access (Access_Source_ID, Direction, Access_Target_ID, Locked, Description) VALUES
#??? room
(1, 'E', 2, TRUE, 'The door is locked, theres a keypad next to it'),
#Boiler room
(2, 'W', 1, False, False),
(2, 'U', 3, False, False),
#Lobby
(3, 'D', 2, False, False),
(3, 'U', 15, False, False),
(3, 'E', 10, False, False),
(3, 'W', 4, False, False),
(3, 'S', 14, TRUE, 'The front door is locked. I have to find a way to open it'),
#West hallway
(4, 'NE', 5, False, False),
(4, 'E', 3, False, False),
(4, 'S', 6, False, False),
(4, 'W', 7, False, False),
#Dining hall
(5, 'SW', 4, False, False),
(5, 'SE', 10, False, False),
#Livingroom
(6, 'N', 4, False, False),
#Kitchen
(7, 'N', 8, False, False),
(7, 'E', 4, False, False),
(7, 'S', 9, False, False),
#Pantry
(8, 'S', 7, False, False),
#Supply closet
(9, 'N', 7, False, False),
#East hallway
(10, 'NW', 5, False, False),
(10, 'E', 12, False, False),
(10, 'S', 11, False, False),
(10, 'W', 3, False, False),
#Garage
(11, 'N', 10, False, False),
#Recreation room
(12, 'W', 10, False, False),
(12, 'S', 13, True, 'The door is locked, it looks like its in pretty bad condition'),
#Bathroom
(13, 'N', 12, False, False),
#Front yard
(14, 'N', 3, False, False),
#2nd floor Hallway
(15, 'D', 3, False, False),
(15, 'E', 18, False, False),
(15, 'S', 20, False, False),
(15, 'W', 16, False, False),
#Master Bedroom
(16, 'E', 15, False, False),
(16, 'S', 17, TRUE, 'I can not move that way. There is a cupboard in the way.'),
#Hidden room
(17, 'N', 16, False, False),
#Library
(18, 'W', 15, False, False),
#Greenhouse
(19, 'E', 20, False, False),
#Storage
(20, 'N', 15, False, False),
(20, 'W', 19, False, False);

INSERT INTO Item(Name,Technical_name,description,room_id,available,takeable, carried) VALUES
( 'Bob doll', 'Bob','A china doll with the name "bob" on its nametag', 11,FALSE,TRUE,FALSE),
( 'Martha doll', 'Martha','A china doll with the name "Martha" on its nametag', 2,FALSE,TRUE,FALSE),
( 'Karen doll', 'Karen','A china doll with the name "Karen" on its nametag', 19,FALSE,TRUE,FALSE),
( 'Tom doll', 'Tom','A china doll with the name "Tom" on its nametag', 12,FALSE,TRUE,FALSE),
( 'Susan doll', 'Susan','A china doll with the name "Susan" on its nametag', 6,FALSE,TRUE,FALSE),
( 'Timmy doll', 'Timmy','A china doll with the name "Timmy" on its nametag', 17,TRUE,TRUE,FALSE),
( 'Easter egg', 'easteregg','Achievment unlocked: OMG an easter egg!', 13,TRUE,TRUE,FALSE),
( 'Front door key', 'Key','Key to freedom.', 5,FALSE,TRUE,FALSE),
( 'Car key', 'Key','it´s a car key', 3,FALSE,TRUE,FALSE),
( 'Closet', 'Closet','It´s a closet, you see a jacket inside it.', 3,TRUE,FALSE,FALSE),
( 'Shoe rack', 'rack','It´s a shoerack with six pairs of shoes', 3,TRUE,FALSE,FALSE),
( 'Painting', 'Painting','It´s a painting of an adult woman. The painting is titled "My beloved Martha".', 4,TRUE,FALSE,FALSE),
( 'Toybox', 'box','It´s a box full of toys', 6,TRUE,FALSE,FALSE),
( 'Sofa', 'sofa','It´s a sofa', 6,FALSE,FALSE,FALSE),
( 'Table', 'table','It´s a table with six seats around it', 5,TRUE,FALSE,FALSE),
( 'Sink', 'Kitchen sink','It´s a sink', 7,TRUE,FALSE,FALSE),
( 'Counter', 'Counter','It´s a counter with kitchen stuff on it', 7,TRUE,FALSE,FALSE),
( 'Freezer', 'Freezer','It´s a freezer', 7,TRUE,FALSE,FALSE),
( 'Refrigerator', 'Fridge','It´s a fridge', 7,TRUE,FALSE,FALSE),
( 'Chore list', 'list','There are chores on the list, Bob: Fix the car, Martha: Make lunch, Karen:Water the plants , Timmy:Watch south park, Susan:Clean up your toys, Tom: Train for darts match', 7,TRUE,TRUE,FALSE),
( 'Garbage bin', 'bin','The bin is full of trash', 7,FALSE,FALSE,FALSE),
( 'Cupboard', 'cupboard', 'It is a big cupboard made of wood.', 17,TRUE,FALSE,FALSE),
( 'Phone', 'phone', 'An old land line phone.', 1, FALSE,FALSE,FALSE),
( 'Computer', 'computer', 'An old computer. ', 1,TRUE,FALSE,FALSE),
( 'Trash bin', 'bin', 'A trash bin, with some rubbish inside. On top there is a piece of paper with some numbers on it.', 1, FALSE, FALSE, FALSE),
( 'Desk', 'Desk', 'A desk with an old landline phone and an old computer on top of it. I wonder what´s under the desk…', 1,TRUE,FALSE,FALSE),
( 'Keyboard', 'keyboard', 'It´s a keyboard', 1,FALSE,FALSE,FALSE),
( 'Books', 'Books for programmers', 'There are several books for programmers', 1,TRUE,FALSE,FALSE),
( 'Parts', 'Computer parts', 'An assortment of old computer parts', 1,FALSE,FALSE,FALSE),
( 'Paper', 'piece of paper', 'A piece of paper with the number 5081 on it. ', 1, FALSE, TRUE, FALSE),
( 'Dinner table', 'table', 'It is a dinner table.', 5, FALSE, FALSE, FALSE),
( 'Billiard table', 'pool table', 'It is a Billiard table. The first hole has balls 1 and 8 inside, second hole: 3, 15; third hole: 12, 13; fourth hole: 2, 6, 10; fifth hole: 5, 7, 14; sixth hole: 4, 9, 11', 12, TRUE, FALSE, FALSE),
( 'Dartboard', 'Dartboard', 'It is a Dartboard.', 12, TRUE, FALSE, FALSE),
( 'Shelf', 'Shelf', 'It is a Shelf.', 11, FALSE, FALSE, FALSE),
( 'Toolbox', 'Toolbox', 'It is a toolbox.', 11, TRUE, FALSE, FALSE),
( 'Car', 'car', 'It is a car, I see a doll inside. Too bad the doors are locked...', 11, TRUE, FALSE, FALSE),
( 'Workbench', 'Workbench', 'It is a workbench.', 11, TRUE, FALSE, FALSE),
( 'Table', 'table', 'It is a round table.', 16,TRUE,FALSE,FALSE),
( 'Chair', 'Chair', 'It´s a chair.', 16,FALSE,FALSE,FALSE),
( 'Carpet', 'Carpet', 'It is a fancy carpet adorned with pictures of horses.', 16,TRUE,FALSE,FALSE),
( 'Bed', 'Bed', 'It is a twinsize bed.', 16,TRUE,FALSE,FALSE),
( 'Cupboard', 'Cupboard', 'You hear static noise from behind the cupboard.', 16,TRUE,FALSE,FALSE),
( 'Sofa', 'Sofa', 'It is a Sofa.', 17,TRUE,FALSE,FALSE),
( 'Television', 'Television', 'It is a Television.', 17,TRUE,FALSE,FALSE),
( 'Bookshelf A', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf B', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf C', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf D', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf E', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf F', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bookshelf G', 'Bookshelf', 'It is a Bookshelf.', 18,TRUE,FALSE,FALSE),
( 'Bench', 'bench', 'A light bench with a newspaper on top', 19,TRUE,FALSE,FALSE),
( 'Window', 'window', 'A big window, it´s boarded on the outside', 19,TRUE,FALSE,FALSE),
( 'ladder - OLD RELIC', 'ladder', 'A step ladder', 19,FALSE,FALSE,FALSE),
( 'Pot', 'pot', 'There is a pot on a shelf and I can’t reach it.', 19,TRUE,FALSE,FALSE),
( 'Block of ice', 'block of ice', 'It is a block of ice, I see something inside.', 7,FALSE,TRUE,FALSE),
( 'Bookmark', 'bookmark', 'Plastic bookmark with text: C-2-17', 7,FALSE,TRUE,FALSE),
( 'Book', 'book', 'It is a blank book.', 18,FALSE,TRUE,FALSE),
( 'Jacket', 'Jacket', 'It´s a stylish leather jacket, I wonder if there´s something in the pockets…', 3, FALSE, FALSE,FALSE);

CREATE USER 'dbuser12'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, INSERT, UPDATE  ON escape_text_adventure.* TO 'dbuser12'@'localhost';
