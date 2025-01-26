import eel
import sys
# let me defend my self here i could easly write my own code here but i was running out of time so i had to use this code from the internet
# Define a function to stop the server
# if my mom saw me codeing instead of studying she would kill me
# i hope she dosent see this
# i hope i dont get caught
# pray for me  , Ameen
@eel.expose
def close_server():
    print("Closing server...")
    sys.exit(0)  # Exit the program gracefully
# Initialize the eel app
eel.init("web")
# Start the app
try:
    eel.start("index.html", block=False)
    
    # Keep the server running
    while True:
        eel.sleep(1)  # Prevent high CPU usage
except SystemExit:
    print("Server stopped successfully.")
except Exception as e:
    print(f"Error: {e}")
#  Allahakbar it worked