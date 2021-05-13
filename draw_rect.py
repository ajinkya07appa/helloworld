import cv2

def draw_rect_key_value(path,key_pair_coordinates):
    image=cv2.imread(path)
    #window_name='Image'
    #color=(255,0,0)
    thickness=2
    
    """key_pair_co_ordinates= [[1,2,3,4], [2,3,4,5]]
    types = ["question","answer"] """
    
    for i in key_pair_coordinates:
        cor_x1 = int(i["question"][0])
		cor_y1 = int(i["question"][1])
		cor_x3 = int(i["question"][2])
		cor_y3 = int(i["question"][3])
        
        start_point=(cor_x1,cor_y1)
        end_point=(cor_x3,cor_y3)
        
        image=cv2.rectangle(image,start_point,end_point,(255,0,0), cv2.FILLED)
        
        #cv2.imshow(window_name,image)
        
        
    for i in key_pair_coordinates:
        cor_x1 = int(i["answer"][0])
		cor_y1 = int(i["answer"][1])
		cor_x3 = int(i["answer"][2])
		cor_y3 = int(i["answer"][3])
        
        start_point=(cor_x1,cor_y1)
        end_point=(cor_x3,cor_y3)
        
        image=cv2.rectangle(image,start_point,end_point,(0,128,0), cv2.FILLED)
        
        #cv2.imshow(window_name,image)
        
    return image
        

def draw_rect_table(path,table_co_ordinates):
    image = cv2.imread(path)
    #window_name='Image'
    color = (0,165,255)
    thickness = 2
    for index1, table in enumerate(table_co_ordinates):
        table_cor_x1 = int(table["cordinates"][0])
		table_cor_y1 = int(table["cordinates"][1])
		table_cor_x3 = int(table["cordinates"][2])
		table_cor_y3 = int(table["cordinates"][3])
        
        start_point = (table_cor_x1,table_cor_y1)

        end_point = (table_cor_x3,table_cor_y3)


        image = cv2.rectangle(image, start_point, end_point, color, thickness)
        
    return image
"""
def draw_rect_key_value():
    image = cv2.imread(r'C:\Users\Ajinkya\Desktop\images\1st qtr 2019-1.jpeg')
    window_name='Image'
    key_pair_coordinates = [[1549, 3240, 3827, 4130]]
    color = (255, 0, 0)
    thickness = 2
    for i in key_pair_coordinates:
        cor_x1 = int(i[0])
        cor_y1 = int(i[1])
        cor_x3 = int(i[2])
        cor_y3 = int(i[3])

        start_point = (cor_x1,cor_y1)

        end_point = (cor_x3,cor_y3)


        image = cv2.rectangle(image, start_point, end_point, color, cv2.FILLED)


    cv2.imshow(window_name, image) 
    


if __name__ == "__main__":
    draw_rect()    
    
    """