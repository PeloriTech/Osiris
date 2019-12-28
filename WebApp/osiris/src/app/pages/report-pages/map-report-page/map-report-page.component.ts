import { Component, OnInit } from '@angular/core';
declare let L;

@Component({
  selector: 'app-dashboard-page',
  templateUrl: './map-report-page.component.html',
  styleUrls: ['./map-report-page.component.css']
})
export class MapReportPageComponent implements OnInit {

  constructor() {

  }

  ngOnInit() {
      const map = L.map('map', {
        zoomControl: false
      }).setView([51.505, -0.09], 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      L.control.zoom({ position: 'topright'}).addTo(map);
  }

}