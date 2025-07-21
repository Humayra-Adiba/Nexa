# #!/usr/bin/env python3

# import sys
# sys.path.append('/home/humayra/Music/Nexa')

# # Import all the functions from nexa.py
# from launchapp import closeappweb, openappweb, minimizeapp

# def test_close_command():
#     print("=== Testing Close Command ===")
#     query = "close tab"
#     print(f"Processing query: '{query}'")
    
#     try:
#         print("About to call closeappweb...")
#         closeappweb(query)
#         print("closeappweb completed successfully")
#         return True
#     except Exception as e:
#         print(f"Error in closeappweb: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# def simulate_main_loop():
#     print("=== Simulating Main Application Logic ===")
#     query = "close tab"
#     print(f"Received query: '{query}'")
    
#     try:
#         # Simulate the exact logic from nexa.py
#         if "close" in query:
#             print("Matched 'close' condition")
#             closeappweb(query)
#             print("Function call completed")
#         else:
#             print("Did not match 'close' condition")
        
#         print("Main loop simulation completed")
#         return True
#     except Exception as e:
#         print(f"Error in main loop simulation: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# if __name__ == "__main__":
#     print("Starting comprehensive debug test...")
    
#     # Test 1: Direct function call
#     success1 = test_close_command()
#     print(f"Direct function test: {'PASSED' if success1 else 'FAILED'}")
#     print()
    
#     # Test 2: Simulate main loop logic
#     success2 = simulate_main_loop()
#     print(f"Main loop simulation: {'PASSED' if success2 else 'FAILED'}")
#     print()
    
#     print("Debug test completed")
