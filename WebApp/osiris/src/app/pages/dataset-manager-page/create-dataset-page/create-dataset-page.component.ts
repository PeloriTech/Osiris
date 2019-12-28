import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

export interface Dataset {
  name: string;
  type: string;
  format: string;
  size: string;
}

const ELEMENT_DATA: Dataset[] = [
  {name: 'alpharetta-energy plant', type: 'orthomosaic', format: 'kml', size: '6.4GB'},
  {name: 'cctv-camera-2', type: 'video', format: 'h264', size: '12.2GB'}
];

@Component({
  selector: 'app-dashboard-page',
  templateUrl: './create-dataset-page.component.html',
  styleUrls: ['./create-dataset-page.component.css']
})
export class CreateDatasetPageComponent implements OnInit {

  displayedColumns: string[] = ['name', 'type', 'format', 'size'];
  dataSource = ELEMENT_DATA;

  constructor(private router: Router) { }

  ngOnInit() {
  }

  logout() {
    this.router.navigate(['/dataset/manager'])
  }

}