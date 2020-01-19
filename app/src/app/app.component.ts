import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  constructor(private http: HttpClient){}
  courses = [];

  ngOnInit(){
    let self = this;
    // this.getCourseInfo();
    console.log(this.reqBody);
  }

  course1 = "";
  course2 = "";
  course3 = "";
  course4 = "";
  course5 = "";

  reqBody = {
    "courses": ["math136", "cs136", "math138", "econ101", "stat230"]
    // "courses": []
  }

  courseInfo;

  getCourseInfo(){
    // this.reqBody.courses.push(this.course1);
    // this.reqBody.courses.push(this.course2);
    // this.reqBody.courses.push(this.course3);
    // this.reqBody.courses.push(this.course4);
    // this.reqBody.courses.push(this.course5);
     console.log(this.reqBody);
     console.log("Sending");
     this.courseInfo =  this.sendReq().then((res)=>{
      
     });
    
  }

  sendReq(){
    return new Promise((resolve, reject) => {
      this.http.post("http://127.0.0.1:5000/getCourses", this.reqBody).subscribe((val) =>{
        console.log(val);
        resolve(val);
        this.courseInfo = val['courses'];
        console.log("Course info");
        console.log(this.courseInfo);
      });
    });
  }
  


}
