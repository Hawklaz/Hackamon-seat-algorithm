
target_coordinates = {'X1': 0, 'Y1': 0,'X2': 0,'Y2': 0} # Dictionary to store coordinates of target square

# defining the coordinates for the seat locations for test video
seat1_coordinates = {'X1': 1516, 'X2': 1950, 'Y1': 643, 'Y2': 1263}
seat2_coordinates = {'X1': 1556, 'X2': 2152, 'Y1': 1042, 'Y2': 1440}
seat3_coordinates = {'X1': 278, 'X2': 853, 'Y1': 725, 'Y2': 1415}
seat4_coordinates = {'X1': 579, 'X2': 927, 'Y1': 495, 'Y2': 1024}

# print(target_coordinates['X1'])

csv_reader = open('DataCSV.csv', 'r')
line_data_list = []
# target_coordinates
frame_count = 0
frame_object_coordinates_list =[]
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
        object_coordinates_list.append(target_coordinates)

    elif line_data[0] == 'b':  # Denotes the start of a new frame with the word box_points
        frame_object_coordinates_list[frame_count] = object_coordinates_list

        # Looping through each object
        for object_coordinate in target_coordinates:

            seat1_error = (object_coordinate['X1'] - seat1_coordinates['X1'])^2 + (object_coordinate['Y1'] - seat1_coordinates['Y1'])^2 + (object_coordinate['X2'] - seat1_coordinates['X2'])^2 (object_coordinate['Y2'] - seat1_coordinates['Y2'])^2
            seat2_error = (object_coordinate['X1'] - seat2_coordinates['X1'])^2 + (object_coordinate['Y1'] - seat2_coordinates['Y1'])^2 + (object_coordinate['X2'] - seat2_coordinates['X2'])^2 (object_coordinate['Y2'] - seat2_coordinates['Y2'])^2
            seat3_error = (object_coordinate['X1'] - seat3_coordinates['X1'])^2 + (object_coordinate['Y1'] - seat3_coordinates['Y1'])^2 + (object_coordinate['X2'] - seat3_coordinates['X2'])^2 (object_coordinate['Y2'] - seat3_coordinates['Y2'])^2
            seat4_error = (object_coordinate['X1'] - seat4_coordinates['X1'])^2 + (object_coordinate['Y1'] - seat4_coordinates['Y1'])^2 + (object_coordinate['X2'] - seat4_coordinates['X2'])^2 (object_coordinate['Y2'] - seat4_coordinates['Y2'])^2

            seat_error_dict = {'Seat 1': seat1_error, 'Seat 2': seat2_error, 'Seat 3':seat3_error, 'Seat 4': seat4_error}
            seat_min_error = min(seat1_error,seat2_error,seat3_error,seat4_error) # get minimum error and seat number
            rms_coordinate_error = seat_min_error**0.5  # square root of minimum error

            if seat_error_dict.get(min(seat_error_dict)) == 'Seat 1':
                coordinate_error_ratio = rms_coordinate_error / ((seat1_coordinates['X1'] ^ 2 + seat1_coordinates['Y1'] ^ 2 + seat1_coordinates['X2'] ^ 2 + seat1_coordinates['Y2'] ^ 2)**0.5)
                if coordinate_error_ratio < error_threshold:
                    seat1_occupied = True
                else:
                    seat1_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 2':
                coordinate_error_ratio = rms_coordinate_error / ((seat2_coordinates['X1'] ^ 2 + seat2_coordinates['Y1'] ^ 2 + seat2_coordinates['X2'] ^ 2 + seat2_coordinates['Y2'] ^ 2)**0.5)
                if coordinate_error_ratio < error_threshold:
                    seat2_occupied = True
                else:
                    seat2_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 3':
                coordinate_error_ratio = rms_coordinate_error / ((seat3_coordinates['X1'] ^ 2 + seat3_coordinates['Y1'] ^ 2 + seat3_coordinates['X2'] ^ 2 + seat3_coordinates['Y2'] ^ 2)**0.5)
                if coordinate_error_ratio < error_threshold:
                    seat3_occupied = True
                else:
                    seat3_occupied = False

            elif seat_error_dict.get(min(seat_error_dict)) == 'Seat 4':
                coordinate_error_ratio = rms_coordinate_error / ((seat4_coordinates['X1'] ^ 2 + seat4_coordinates['Y1'] ^ 2 + seat4_coordinates['X2'] ^ 2 + seat4_coordinates['Y2'] ^ 2)**0.5)
                if coordinate_error_ratio < error_threshold:
                    seat4_occupied = True
                else:
                    seat4_occupied = False

        object_coordinates_list = []
        frame_count += 1

