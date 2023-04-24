INSERT INTO public.point_types(
	"Guid", name, description)
	VALUES ('4a5bebc2-0cee-4094-9c35-6400dbc97670', 'A', ''),
	('023dfccf-f398-4961-89e6-ae906b83b550', 'A1', ''),
	('8d429c15-8bdf-4b8d-b79e-4263c8d0c9f5', 'ANS', ''),
	('6532698d-752d-42d0-a170-a279232d67ef', 'AR', ''),
	('b7fb5f16-a24d-4e64-8555-3a4b1b4e32f6', 'B', ''),
	('e038ceb5-af53-47e9-a596-9a1c517760dd', 'B1', ''),
	('ee5acf79-a6f1-4ca6-b391-7ca08b580926', 'BR', ''),
	('8075743f-1be8-45b7-930c-de01e0292de9', 'DT', ''),
	('6c48f468-53f0-4043-b0b1-3044441a2258', 'En', ''),
	('acc34581-5925-472d-815c-c0aa450d9e52', 'Go', ''),
	('3bdcf123-dc08-484e-a119-8023eefc0814', 'Me', ''),
	('ff2e65d9-1f50-44a6-b706-47d6e6ff974c', 'Mn', ''),
	('01096d87-b09e-4d0d-bb88-32a9c4ca8288', 'N', ''),
	('4f302c4a-fa59-4542-b4b5-08e41eeb7192', 'Or', ''),
	('f00a7921-49a1-48a4-a5be-48c238bfc660', 'PAC', ''),
	('d8c3357f-6f18-437d-a10d-bc4deff61eb7', 'Pg', ''),
	('2393a6c8-e351-4bd1-b0da-c942a17cebb3', 'PNS', ''),
	('020f3e65-e88c-4c81-b9c4-a1c56fc8a06d', 'Po', ''),
	('d2d3a635-2ef2-4db2-a238-20d79129b97e', 'S', '');
	
INSERT INTO public.line_types(
	"Guid", name, description)
	VALUES ('25c52bab-255d-46e1-ae1a-93ddbe42e94b', 'FH', ''),
	('4f8b2f54-3cc2-4c77-87b5-01a5bb83d724', 'NA', ''),
	('5e0d5112-30b7-4fe0-890c-9dbce8b8e59c', 'NB', ''),
	('fad0a0a5-7385-4581-82dd-50f5ec5c53e0', 'SN', ''),
	('3ac95839-2771-42be-a150-396488c60d45', 'A1AR', ''),
	('8b1617b7-90f0-4c21-8102-0bede233a471', 'NPg', ''),
	('23ebcf69-d534-4037-81fe-3fdc0d83e273', 'MP', ''),
	('80eafee5-c5d0-4c69-8e79-3ff8e217a496', 'B1BR', '');
	
INSERT INTO public.param_types(
	"Guid", name, description, min, max)
	VALUES ('33a9bc9c-142a-4f2a-bbec-3da33e17e29f', 'FN_NA', '', 87, 93),
	('c6e1982a-861b-4588-919d-ff5d5c2faeec', 'SNA', '', 80, 84),
	('eff8fb0a-68c3-4477-a43f-5cb97e4b163c', 'ANB', '', 0, 4),
	('01b5f198-3c26-47a6-ba55-be576a24d921', 'SN_A1AR', '', 99, 105),
	('7b8e2708-cdb3-4988-b6d2-fb5f703ce598', 'SNB', '', 78, 82),
	('c78c136d-6536-4d45-bef3-957c83512d9e', 'FH_NPg', '', 87, 93),
	('12941443-33fa-4c45-9398-0ad0ea08edea', 'IMPA', '', 86, 94),
	('11d8c727-122b-4e04-bda9-c3c3ccebf133', 'FMA', '', 21, 31);