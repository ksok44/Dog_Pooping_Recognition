from google_images_download import google_images_download

def downloadImages(response, query, o_path, c_path):
    '''
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded - default is 100
    # print urls is to print the image file url 
    # size is the image size which can be specified manually ("large, medium, icon") 
    # aspect_ratio denotes the height width ratio of images to download. ("tall, square, wide, panoramic") 
    # output_directory specifies the directory to save the images to
    # chromedirver specifies the path of the chromedriver, which is needed to download more than 100 photos at once
    '''
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":200, 
                 "print_urls":False, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic",
                 "output_directory": o_path,
                 "chromedriver": c_path}
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        print('Error, no search results found')

def main():
    
    # Creating an object
    response = google_images_download.googleimagesdownload()  

    # Search queries
    search_queries = ['dog outside']
    
    # File output path
    o_path = 'G:/My Drive/Analytic Apps/DApps_Project/Images_Staging/'
    
    # Chrome driver path
    c_path = 'C:/Users/kobys/Desktop/chromedriver.exe'

    for query in search_queries:
        downloadImages(response, query, o_path, c_path)
        print()
    
main()

