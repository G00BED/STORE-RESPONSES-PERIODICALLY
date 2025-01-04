#Stores a functions response to txt every 5 minutes
def store_responses_periodically(function , filename="responses.txt", interval=300):
    """
    Stores responses from a function call in a text file every `interval` seconds.

    Parameters:
    - function (callable): The function to call for getting responses.
    - filename (str): Name of the file where responses will be saved. Default is 'responses.txt'.
    - interval (int): Time interval between calls in seconds. Default is 300 (5 minutes).

    Returns:
    None
    """
    ticker = 0 

    try:
        while True:

            # Call the function to get the response
            response = function()
            
            # Write the response to the file
            with open(filename, "a") as file:  # Append mode to preserve earlier responses
                file.write(response + "\n")
            
            ticker += 1
            print(f"BOT SAYS - {response} \n {ticker} RESPONSES GENERATED THIS SESSION.")   
            
            # Wait for the specified interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("BOT HAS STOPPED")
    except Exception as e:
        print(f"ERROR : {e}")

#Call the function
store_responses_periodically(ENTER FUNCTION HERE)
