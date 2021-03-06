/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Main;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

/**
 *
 * @author yudi
 */
public class Client {

    public static void comecar(GUIClient gui, Socket s) {

        TaskThreadClient c = new TaskThreadClient(gui, s);

    } //main
} //class TCPClient

class TaskThreadClient extends Thread {

    DataInputStream in;
    Socket clientSocket;
    GUIClient gui;

    public TaskThreadClient(GUIClient gui, Socket aClientSocket) {
        this.gui = gui;

        try {
            clientSocket = aClientSocket;
            in = new DataInputStream(clientSocket.getInputStream());
            /* Configurar outputStream para ler do socket */

            this.start();
            /* inicializa a thread */

        } catch (IOException e) {
            System.out.println("Connection:" + e.getMessage());
        } //catch
    } //construtor

    /* metodo executado ao iniciar a thread - start() */
 /* Metodo executado quando a thread e iniciada */
    public void run() {

        try {
            while (true) {

                String data = in.readUTF();
                if (!data.equals(this.gui.getText())) {
                    this.gui.setText(data);
                }

            }
            /* While */

        } catch (EOFException e) {
            System.out.println("EOF: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("leitura: " + e.getMessage());
        } //catch

    } //run

} //class

