import sys
import grpc

# Import the generated files from the resources folder
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc

def main():
    # Use the first argument as the Warehouse ID
    warehouse_id = sys.argv[1] if len(sys.argv) > 1 else "001-DEFAULT"

    # Connect to the Java server
    with grpc.insecure_channel("localhost:50051") as channel:
        # Note: The stub name must match your .proto service name
        stub = pb2_grpc.DataWarehouseServiceStub(channel)

        # Create the request
        request = pb2.WarehouseRequest(warehouseID=warehouse_id)

        print(f"--- Requesting Data for Warehouse: {warehouse_id} ---")

        try:
            # Call the remote method
            response = stub.getWarehouseData(request)

            # Print the results from the Java Server
            print(f"Response from Server:")
            print(f"  Warehouse Name: {response.warehouseName}")
            print(f"  City:           {response.warehouseCity}")
            print(f"  Products in Stock:")
            for p in response.productData:
                print(f"    -> [{p.productID}] {p.productName}: {p.productQuantity} units")

        except grpc.RpcError as e:
            print(f"Error: Could not reach the server. {e.details()}")

if __name__ == "__main__":
    main()