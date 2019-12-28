import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MapReportPageComponent } from "./map-report-page.component";

describe('MapReportPageComponent', () => {
  let component: MapReportPageComponent;
  let fixture: ComponentFixture<MapReportPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MapReportPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MapReportPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
