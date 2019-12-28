import { Component, OnInit } from '@angular/core';

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
  templateUrl: './dataset-page.component.html',
  styleUrls: ['./dataset-page.component.css']
})
export class DatasetPageComponent implements OnInit {

  displayedColumns: string[] = ['name', 'type', 'format', 'size'];
  dataSource = ELEMENT_DATA;

  constructor() { }

  ngOnInit() {
  }

}