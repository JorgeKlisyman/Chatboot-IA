import { Component, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent {
  userInput: string = '';
  @ViewChild('chatBox') chatBox!: ElementRef;

  constructor(private http: HttpClient) {}

  sendMessage() {
    const input = this.userInput.trim();
    if (!input) return;

    this.appendUserMessage(input);
    this.userInput = '';

    this.http.post<any>('http://127.0.0.1:5000/perguntar', { pergunta: input }).subscribe({
      next: data => {
        this.appendBotMessage(data.resposta);
        this.scrollChatToBottom();
      },
      error: err => {
        this.appendBotMessage('Erro ao obter resposta.');
        console.error('Erro:', err);
      }
    });
  }

  appendUserMessage(message: string) {
    const div = document.createElement('div');
    div.className = 'user-message';
    div.textContent = message;
    this.chatBox.nativeElement.appendChild(div);
    this.scrollChatToBottom();
  }

  appendBotMessage(message: string) {
    const div = document.createElement('div');
    div.className = 'bot-message';
    div.textContent = message;
    this.chatBox.nativeElement.appendChild(div);
    this.scrollChatToBottom();
  }

  scrollChatToBottom() {
    this.chatBox.nativeElement.scrollTop = this.chatBox.nativeElement.scrollHeight;
  }
}
