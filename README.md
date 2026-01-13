# Middleware Engineering "DEZSYS_GK_HELLOWORLD_GRPC"

## Aufgabenstellung
Dieses Projekt zeigt, wie das gRPC-Framework genutzt werden kann, um einen sprachübergreifenden Remote Procedure Call (RPC) zwischen einem Java-Server sowie Java- und Python-Clients zu realisieren.

## Theoretische Grundlagen

### Was ist gRPC und warum ist es sprach- und plattformunabhängig?

gRPC ist ein von Google entwickeltes RPC-Framework, das es ermöglicht, Funktionen auf einem entfernten Server so aufzurufen, als wären sie lokal verfügbar. Im Gegensatz zu REST, das auf URLs und JSON setzt, nutzt gRPC kompakte, binäre Nachrichten.

Die Sprachunabhängigkeit entsteht durch **Protocol Buffers**. Eine einzige `.proto`-Datei dient dabei als gemeinsamer Vertrag, aus dem automatisch Code für verschiedene Programmiersprachen (Java, Python, Go usw.) generiert wird.

### RPC-Lebenszyklus aus Sicht des Clients

1. **Aufruf**: Der Client ruft eine Methode auf einem lokal generierten Stub auf.
2. **Serialisierung**: Parameter werden in Protocol-Buffer-Form umgewandelt.
3. **Übertragung**: Die Binärnachricht wird an den Server gesendet.
4. **Deserialisierung**: Der Server entpackt die Nachricht und ruft die zugehörige Funktion auf.
5. **Verarbeitung**: Die Serverlogik erzeugt das Ergebnis.
6. **Antwort**: Das Ergebnis wird serialisiert und an den Client zurückgeschickt.

### Workflow von Protocol Buffers

1. **Definition**: In einer `.proto`-Datei werden Services und Nachrichtenstrukturen beschrieben.
2. **Generierung**: `protoc` erzeugt aus der Datei automatisch Klassen für die gewünschte Sprache.
3. **Nutzung**: Diese Klassen werden im Code verwendet, um Nachrichten zu erzeugen, zu senden und zu empfangen.

### Vorteile von Protocol Buffers

* **Sehr effizient**: Binärformat ist kompakt und schnell.
* **Strenge Typisierung**: Fehler durch unklare Datenstrukturen werden vermieden.
* **Saubere API-Weiterentwicklung**: Neue Felder können hinzugefügt werden, ohne Kompatibilität zu brechen.

### Wann eignen sich Protocol Buffers nicht?

* Wenn Daten direkt vom Menschen lesbar sein müssen.
* Für klassische Browseranwendungen, außer mit Hilfstools wie gRPC-Web.

### Beispiele für Datentypen in Protocol Buffers

* `string`
* `int32`
* `repeated` (Liste eines Datentyps)

---

## Implementierung

Start HelloWorldServer (Java)  
`gradle clean build`  
`gradle runServer`

Start HelloWorldClient (Java)  
`gradle runClient`
  

-------------------------------- Python 

Add grpcio packages  
`pip3 install grpcio grpcio-tools`  

Compile .proto file  
`python3 -m grpc_tools.protoc -I src/main/proto  
  --python_out=src/main/resources  
  --grpc_python_out=src/main/resources  
  src/main/proto/hello.proto`  

Start HelloWorldClient (Python)  
`python3 src/main/resources/helloWorldClient.py`  

---

Ziel war es, das HelloWorld-Projekt so zu erweitern, dass vollständige DataWarehouse-Daten übertragen werden können.

### Schritt 1: Anpassung der `.proto`-Datei

Die ursprüngliche Datei wurde vollständig ersetzt. Der neue Service sowie die benötigten Datenstrukturen wurden definiert.

*(Proto-Code bleibt unverändert)*

Nach der Anpassung wurden mit
`./gradlew clean build`
die neuen Java-Klassen generiert.

### Schritt 2: Anpassung der Java-Implementierung

#### `DataWarehouseServiceImpl.java`

Die alte HelloWorld-Service-Klasse wurde entfernt und durch eine neue Service-Implementierung ersetzt.

*(Code bleibt gleich)*

#### `HelloWorldServer.java`

Der Server lädt nun den neuen DataWarehouse-Service anstelle des ursprünglichen HelloWorld-Services.

#### `HelloWorldClient.java`

Der Client nutzt jetzt die neuen Nachrichtenstrukturen und ruft `getWarehouseData()` auf.

### Schritt 3: Test der Java-Komponenten

Der Server wurde in einem Terminal gestartet, der Client in einem zweiten ausgeführt.

Ausgabe und Ablauf funktionierten wie erwartet.

### Schritt 4: Anpassung des Python-Clients

Um die Sprachkompatibilität zu demonstrieren, wurde auch der Python-Client an den neuen Vertrag angepasst. Dazu gehörten:

* Installation der benötigten Pakete (`grpcio`, `grpcio-tools`)
* Regeneration der Python-Dateien mittels `grpc_tools.protoc`
* Anpassung der Client-Logik

Der Python-Client konnte erfolgreich Daten vom Java-Server abfragen.

---

## Fehler
- Dateipfad enthielt Sonderzeichen

## Quellen
- Syt-Unterlagen
