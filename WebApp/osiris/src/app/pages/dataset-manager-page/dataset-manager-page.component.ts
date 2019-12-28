import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

export interface Dataset {
  id: string;
  name: string;
  type: string;
  format: string;
  size: string;
}

const ELEMENT_DATA: Dataset[] = [
  { id: '1', name: 'alpharetta-energy plant', type: 'orthomosaic', format: 'kml', size: '6.4GB'},
  { id: '2', name: 'cctv-camera-2', type: 'video', format: 'h264', size: '12.2GB'}
];

@Component({
  selector: 'app-dashboard-page',
  templateUrl: './dataset-manager-page.component.html',
  styleUrls: ['./dataset-manager-page.component.css']
})
export class DatasetManagerPageComponent implements OnInit {

  displayedColumns: string[] = ['name', 'type', 'format', 'size', 'go'];
  dataSource = ELEMENT_DATA;

  constructor(private router: Router) { }

  ngOnInit() {
  }

  open_dataset(){
    this.router.navigate(['/dataset/view']);
  }

}