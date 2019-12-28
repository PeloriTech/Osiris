import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatasetManagerPageComponent } from './dataset-manager-page.component';

describe('DatasetPageComponent', () => {
  let component: DatasetManagerPageComponent;
  let fixture: ComponentFixture<DatasetManagerPageComponent>;
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatasetManagerPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatasetManagerPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
