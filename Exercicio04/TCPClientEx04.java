/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Exercicio04;

import java.io.DataInputStream;
import java.io.EOFException;
import java.io.IOException;
import java.net.Socket;

/**
 *
 * @author yudi
 */
public class TCPClientEx04 {

    public static void comecar(GUIClient gui, Socket s) {

        TaskThreadEx4 c = new TaskThreadEx4(gui, s);

    } //main
} //class TCPClient

class TaskThreadEx4 extends Thread {

    DataInputStream in;
    Socket clientSocket;
    GUIClient gui;

    public TaskThreadEx4(GUIClient gui, Socket aClientSocket) {
        this.gui = gui;

        try {
            clientSocket = aClientSocket;
            in = new DataInputStream(clientSocket.getInputStream()); /* Configurar outputStream para ler do socket */

            this.start();  /* inicializa a thread */

        } catch (IOException e) {
            System.out.println("Connection:" + e.getMessage());
        } //catch
    } //construtor

    /* metodo executado ao iniciar a thread - start() */
    /* Metodo executado quando a thread e iniciada */
    @Override
    public void run() {

        try {
            while (true) {

                String data = in.readUTF();
                if (data.equals("/sair")) {
                    gui.disableBotoes();
                } else {
                    this.gui.setText(data);
                }

            } /* While */

        } catch (EOFException e) {
            System.out.println("EOF: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("leitura: " + e.getMessage());
        } //catch

    } //run

} //class

