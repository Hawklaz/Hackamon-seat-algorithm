
target_coordinates = {'X1': 0.0, 'Y1': 0.0, 'X2': 0.0, 'Y2': 0.0}  # Dictionary to store coordinates of target square

# defining the coordinates for the seat locations for test video
seat1_coordinates = {'X1': 1516.0, 'X2': 1950.0, 'Y1': 643.0, 'Y2': 1263.0}
seat2_coordinates = {'X1': 1556.0, 'X2': 2152.0, 'Y1': 1042.0, 'Y2': 1440.0}
seat3_coordinates = {'X1': 278.0, 'X2': 853.0, 'Y1': 725.0, 'Y2': 1415.0}
seat4_coordinates = {'X1': 579.0, 'X2': 927.0, 'Y1': 495.0, 'Y2': 1024.0}

# print(target_coordinates['X1'])

csv_reader = open('DataCSV.csv', 'r')
line_data_list = []
# target_coordinates
frame_count = 0
frame_object_coordinates_list = []
object_coordinates_list = []
rms_coordinate_error = 0
seat1_error = 0
seat2_error = 0
seat3_error = 0
seat4_error = 0
seat1_occupied = False
seat2_occupied = False
seat3_occupied = False
seat4_occupied = False
error_threshold = 0.15 # error threshold for seat determining if seat is occupied
seat_error_dict = {}
seat_min_error = 0
seat_occupied_list = []

for line_data in csv_reader: # iterates for each object
    # print(len(line_data_list))
    # line_data_list = line_data.split(sep=',')
    # print(len(line_data_list))
    # print(type(line_data_list))
    # # target_coordinates['X1'] = line_data_list[]

    if line_data[0] == '[':
        # print('Yes')
        # print(line_data)
        line_data = line_data.lstrip('[')
        # print('After lstrip',line_data)
        line_data = line_data.strip()
        # print('After strip',line_data)
        line_data = line_data.rpartition(']')[0]
        line_data = line_data.strip()
        print(line_data)
        target_coordinates['X1'] = line_data.split()[0]
        target_coordinates['Y1'] = line_data.split()[1]
        target_coordinates['X2'] = line_data.split()[2]
        target_coordinates['Y2'] = line_data.split()[3]
        print(target_coordinates)
        object_coordinates_list.append(target_coordinates)  # appending object coordinates to list. This list is cleared every new frame

    elif line_data[0] == 'b':  # Denotes the start of a new frame with the word box_points
        frame_object_coordinates_list.append(object_coordinates_list)

        # By the time we execute below here, all objects in the frame are in the list frame_object_coordinates_list
        # Looping through each object to identify error against each seat
        for object_coordinate in target_coordinates:

            seat1_error = (object_coordinate.get('X1') - seat1_coordinates.get('X1'))**2 + (object_coordinate.get('Y1') - seat1_coordinates.get('Y1'))**2 + (object_coordinate.get('X2') - seat1_coordinates.get('X2'))**2 (object_coordinate.get('Y2') - seat1_coordinates.get('Y2'))**2
            seat2_error = (object_coordinate.get('X1') - seat2_coordinates.get('X1'))**2 + (object_coordinate.get('Y1') - seat2_coordinates.get('Y1'))**2 + (object_coordinate.get('X2') - seat2_coordinates.get('X2'))**2 (object_coordinate.get('Y2') - seat2_coordinates.get('Y2'))**2
            seat3_error = (object_coordinate.get('X1') - seat3_coordinates.get('X1'))**2 + (object_coordinate.get('Y1') - seat3_coordinates.get('Y1'))**2 + (object_coordinate.get('X2') - seat3_coordinates.get('X2'))**2 (object_coordinate.get('Y2') - seat3_coordinates.get('Y2'))**2
            seat4_error = (object_coordinate.get('X1') - seat4_coordinates.get('X1'))**2 + (object_coordinate.get('Y1') - seat4_coordinates.get('Y1'))**2 + (object_coordinate.get('X2') - seat4_coordinates.get('X2'))**2 (object_coordinate.get('Y2') - seat4_coordinates.get('Y2'))**2

            seat_error_dict = {'Seat 1': seat1_error, 'Seat 2': seat2_error, 'Seat 3':seat3_error, 'Seat 4': seat4_error}
            seat_min_error = min(seat1_error,seat2_error,seat3_error,seat4_error)  # get minimum error and seat number
            rms_coordinate_error = seat_min_error**0.5  # square root of minimum error

            # Checking which seat has the minimum error for that particular object (could be occupied)
            if seat_error_dict.get(min(seat_error_dict)) == 'Seat 1':
                coordinate_error_ratio = rms_coordinate_error / ((seat1_coordinates.get('X1') ** 2 + seat1_coordinates.get('Y1') ** 2 + seat1_coordinates.get('X2') ** 2 + seat1_coordinates.get('Y2') ** 2)**0.5)
                if coordinate_error_ratio < error_threshold:   # checking if the seat is actually occupied
                    seat1_occupied = True
                else:
                    seat1_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 2':
                coordinate_error_ratio = rms_coordinate_error / ((seat2_coordinates.get('X1') ** 2 + seat2_coordinates.get('Y1') ** 2 + seat2_coordinates.get('X2') ** 2 + seat2_coordinates.get('Y2') ** 2)**0.5)
                if coordinate_error_ratio < error_threshold:   # checking if the seat is actually occupied
                    seat2_occupied = True
                else:
                    seat2_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 3':
                coordinate_error_ratio = rms_coordinate_error / ((seat3_coordinates.get('X1') ** 2 + seat3_coordinates.get('Y1') ** 2 + seat3_coordinates.get('X2') ** 2 + seat3_coordinates.get('Y2') ** 2)**0.5)
                if coordinate_error_ratio < error_threshold:   # checking if the seat is actually occupied
                    seat3_occupied = True
                else:
                    seat3_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 4':
                coordinate_error_ratio = rms_coordinate_error / ((seat4_coordinates.get('X1') ** 2 + seat4_coordinates.get('Y1') ** 2 + seat4_coordinates.get('X2') ** 2 + seat4_coordinates.get('Y2') ** 2)**0.5)
                if coordinate_error_ratio < error_threshold:   # checking if the seat is actually occupied
                    seat4_occupied = True
                else:
                    seat4_occupied = False
            else:
                seat1_occupied = False
                seat2_occupied = False
                seat3_occupied = False
                seat4_occupied = False

            # finished checking which seat has the minimum error and is therefore occupied

            # appending list of dictionaries which include seat occupancy.
            # Frame is denoted by the index of this list
            seat_occupied_list.append(
                {'seat1': seat1_occupied, 'seat2': seat2_occupied, 'seat3': seat3_occupied, 'seat4': seat4_occupied})

        object_coordinates_list = []
        frame_count += 1

csv_reader.close()
csv_writer = open('OutputData.csv', 'w')

data_dict_line ={}

for data_dict_line in seat_occupied_list:
    csv_writer.write(str(data_dict_line))

csv_writer.close()


