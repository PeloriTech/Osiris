import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateNewPipeComponent } from './create-new-pipe.component';

describe('CreateNewPipeComponent', () => {
  let component: CreateNewPipeComponent;
  let fixture: ComponentFixture<CreateNewPipeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateNewPipeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateNewPipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
