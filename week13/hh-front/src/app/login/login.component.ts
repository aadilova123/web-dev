import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '../authentication.service';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string;
  password: string;
  constructor(private authService: AuthenticationService) { }

  ngOnInit(): void {
  }

  login() {
    this.authService.login(this.username, this.password)
      .subscribe(
        response => {
          localStorage.setItem('token', response.token);
        },
        error => console.log(error)
      );
  }

  logout() {
    localStorage.clear();
  }
}
