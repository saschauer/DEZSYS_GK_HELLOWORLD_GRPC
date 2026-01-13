import grpc.datawarehouse.*;
import io.grpc.stub.StreamObserver;

public class DataWarehouseServiceImpl extends DataWarehouseServiceGrpc.DataWarehouseServiceImplBase {

    @Override
    public void getWarehouseData(WarehouseRequest request, StreamObserver<WarehouseData> responseObserver) {
        System.out.println("Anfrage für Warehouse-ID erhalten: " + request.getWarehouseID());

        Product product1 = Product.newBuilder()
                .setProductID("12-998432")
                .setProductName("Alpen Bergkaese Premium")
                .setProductQuantity(780)
                .build();

        WarehouseData response = WarehouseData.newBuilder()
                .setWarehouseID(request.getWarehouseID())
                .setWarehouseName("Salzburg Nordlager (gRPC)")
                .setWarehouseCity("Salzburg")
                .addProductData(product1)
                .build();
        System.out.println("Anfrage bekommen: " + request);
        System.out.println("Anfrage gefunden: " + response);
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}